library(tidyverse)
library(ggplot2)

num_subjects = 20

# set up and format data frame

data <- NULL

for (i in 1:num_subjects) {
  d_i <- read.csv(paste("data/", i, ".csv", sep=""), header=T)
  d_i <- d_i[ !(d_i$id == -1), ]
  d_i <- d_i  %>%
    select(-X) %>%
    rename(subject = id, rt = RT) %>% 
    mutate(size = recode(size, 
                         "0" = "LS", 
                         "1" = "HS"),
           rt = ceiling(rt),
           accuracy = round(correct / 64 * 100, 2))
  data <- rbind(data, d_i)
}
remove(d_i, i)

# reorder
data <- data[, c("subject", "q1", "q2", "q3", "q4", "size", "freq", "rt", "correct", "accuracy")]

data = data %>%
  group_by(freq,subject,size) %>%
    summarise(mean_rt=mean(rt), sd=sd(rt),
              mean_accuracy=mean(accuracy), sd=sd(accuracy))

aov(mean_accuracy ~ size * freq + Error(factor(subject)), data=data) %>% summary()

library(tidyverse)
library(ggplot2)

num_subjects = 20

# set up and format data frame

data <- NULL

for (i in 1:num_subjects) {
  d_i <- read.csv(paste("chunking/data/", i, ".csv", sep=""), header=T)
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

################################################################################

data_basic <- data %>% select(size, freq, rt, accuracy)

data_basic %>%
  group_by(size, freq) %>% 
  summarize(mean_acc = mean(accuracy),
            sd_acc = sd(accuracy),
            mean_rt = mean(rt),
            sd_rt = sd(rt))

# ANOVA test
aov(accuracy ~ size*freq + Error(subject), data=data) %>%  summary()

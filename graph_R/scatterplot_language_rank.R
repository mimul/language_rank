if (!require(calibrate)) install.packages('calibrate')
library(calibrate)

con <- 
 url("http://mimul.com/pebble/default/files/blog/language_rank.csv")
rank_data <- read.csv(con,sep=",",head=TRUE)

plot(rank_data$github.rank,rank_data$so.rank,
       main="programming languages popularity",
       xlab="Rank On GitHub",
       ylab="Rank On StackOverflow", bg="yellow", col="red")
abline(lm(github.rank ~ so.rank, data= rank_data), col= "blue")
textxy(rank_data$github.rank,rank_data$so.rank,rank_data$Language)
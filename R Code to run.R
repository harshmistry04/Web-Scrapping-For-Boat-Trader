data1 <- read.csv('Cleaned data.csv', header = T)
attach(data1)

pairs(data1);

par(mfrow=c(3,3)); ##this command plots 6 graphs on one page
for (i in 1:7){
    hist(as.numeric(data1[,i+1]),main=paste(names(data1)[i+1]),xlab="")}

library(MASS);
par(mfrow=c(1,1),cex=.5);
parcoord(data1[,2:8],lty=2,col=grey(.3))

mod1 <- hclust(dist(data1[,2:8]), "ave");
plot(mod1,labels=as.character(data1[,1]));
clus<- rect.hclust(mod1, k=4, border="red");

mod1 <- hclust(dist(data1[,2:8]), "ave");
plot(mod1,labels=as.character(data1[,1]));
clus<- rect.hclust(mod1, k=3, border="red");
##################################################################################
install.packages("scatterplot3d")

library(scatterplot3d);
arning message:
ackage ‘scatterplot3d’ was built under R version 3.2.2 
par(mfrow=c(1,1));
scatterplot3d(Year,Length,Total.Power,col.grid="lightblue", highlight.3d=TRUE,pch=20,lwd=3);
par(mfrow=c(1,1));
scatterplot3d(Price,Length,Total.Power,col.grid="lightblue", highlight.3d=TRUE,pch=20,lwd=3);
###########################################################################
Elbow plot
#investigate different number of K
par(mfrow=c(1,1),cex=1)
K<-20; elbow<- array(NA,c(K,1));
for (i in 2:K){mod.x <- kmeans(dist(data1[,2:8]),i,iter.max=20);
elbow[i]<- mean(mod.x$withinss);}
plot(seq(1,K),elbow,type="b",pch=17,xlab="Number of Clusters",ylab="")

K means Clustering with 3 clusters
par(mfrow=c(1,1),cex=0.5)
mod2 <- kmeans(dist(data1[,2:8]),3,iter.max=20)
plot(data1[,2:8], col = mod2$cluster,pch=15)
clus <- as.numeric(mod2$cluster)

g.mean <-  apply(data1[,2:8],2,mean);
g.sd   <-  apply(data1[,2:8],2,sd);

cluster_means <- NULL; cluster_sds <- NULL;

for (i in 1:3){
    cluster_means[[i]]<-(apply(data1[as.numeric(which(clus==i)),2:8],2,mean)-g.mean)/g.sd;}

par(mfrow=c(1,1))
plot(seq(1,7),cluster_means[[1]],pch=c("1","2","3","4","5","6","7"),col=2,cex=1.2,
     xlim=c(1,7),ylim=c(-0.09,7),xlab="",ylab="Means",type="b")
for (i in 2:3){lines(seq(1,7),cluster_means[[i]],pch=c("1","2","3","4","5","6","7")
                     ,col=i+1,cex=1.2,type="b")}
leg.txt <- c("Clus1","Clus2","Clus3");
legend(1,6,leg.txt,lty=c(1,1,1),col=c(2,3,4));
##############################################################################
For non parametric regression model
Lmod1 <- lm(Price ~ Year + Class + Length + Total.Power + Engine.Hours + Propulsion.Type)
summary(Lmod1)

library(mgcv)

mod3 <- gam(Price ~ s(Year) + s(Length) + s(Total.Power) + s(Engine.Hours))
plot(mod3)
summary(mod3)

mod4 <- gam(Price ~ s(Year) + s(Length) + Total.Power + Engine.Hours)
summary(mod4)
#########################################################################
#logistic regression model
library(lattice);

data3 <- read.csv('Cleaned data - Logistic regression2.csv',header = T)
glmod1 <- glm(data3$Price ~ data3$Year + data3$Class + data3$Length + data3$Total.Power + data3$Engine.Hours + data3$Propulsion.Type, family = binomial)
summary(glmod1)
glmod2 <- glm(data3$Price ~ data3$Year + data3$Class + data3$Length + data3$Propulsion.Type, family = binomial)
summary(glmod2)
glmod3 <- glm(data3$Price ~ data3$Year + data3$Length + data3$Propulsion.Type, family = binomial)
summary(glmod3)

bwplot(data3$Pr1ce~data3$Length);
dotplot(data3$Price~data3$Length,horizontal=T);








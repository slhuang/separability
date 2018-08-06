#!/usr/bin/env Rscript

name = "Delys_Thyroid_Cancer.txt" #"BRD-K85133207.txt (EXP1)" 	 	#BRD-K85133207.txt \n 			 	 		
fx = "GO_0000302"	#"201719_s_at"				
fy ="GO_0007155" #"202720_at"    


px <- c(5.089839,1.614713)
 #(20.230740,9.662562) # the first line in "meta.txt" 
py <- c (4.478331,1.525167) #(1,11.236356)  # the second line in "meta.txt"
estimate <- read.csv("ratioHist.txt",sep="\t",header = TRUE,check.names=FALSE)
rnames <- estimate[,1]
est_matrix <- data.matrix(estimate[,2:ncol(estimate)])
rownames(est_matrix) <- rnames
my_palette <- colorRampPalette(c("red", "white", "blue"), space="rgb")(n=300) 
my_break <- c(seq(-100, 0, length.out=300/2)-0.5, 0, seq(0, 100, length.out=300/2)+0.5) #300 100
png("../fig/ratioHist_msig_1.pdf", width=4, height=4, units="in", res=300,pointsize = 12)
est_heatmap <- heatmap(est_matrix, Rowv = NA, Colv=NA, col = my_palette, breaks=my_break,  xlab = fx, ylab =fy,  main = name, scale ="none", margins=c(4.2,4.5),add.expr =points(px,py,col=c("blue","darkred")))
#abline(v=0,col="red")
#abline(h=0,col="red")
#points(px,py)
#abline(a=1.856648,b=-1.122625,col="red")  	 
#title(xlab=fx
# ,mgp=c(-2,-1,-5))
dev.off()



# 	0.01	0.42	0.83	1.24	1.66	2.07	2.48	2.89	3.31	3.72	4.13	4.55	4.96	5.37	5.78	6.20	6.61	7.02	7.43	7.85
# 0.01	-82	-21	-12	-16	-12	-4	-3	2	4	6	-5	7	7	8	5	9	5	-3	-3	10
# 0.53	-24	-16	-8	-10	-9	-8	-4	9	-3	-7	7	9	-5	9	6	9	-3	-2	-3	16
# 1.06	-14	-13	-10	12	7	12	12	10	10	10	-5	5	-5	5	5	6	9	6	-3	21
# 1.59	-12	-11	-9	11	-6	6	5	-7	7	-4	4	-4	6	-3	6	-4	-3	6	6	19
# 2.12	0	3	13	13	5	7	7	7	4	-4	-4	8	5	6	-4	-3	-2	-3	-3	15
# 2.64	8	9	13	3	9	-5	11	-5	5	-4	10	-3	9	-2	-2	-3	-2	6	-3	13
# 3.17	-7	-1	-8	9	8	8	5	-4	-2	-3	6	-1	-3	-3	-2	-2	-1	6	-2	4
# 3.70	3	-6	10	4	10	4	-3	-3	6	9	-4	9	-1	-2	9	-2	6	-3	-1	11
# 4.22	5	14	8	8	-4	8	-3	-3	-2	6	6	6	-2	-2	0	-2	-1	-2	6	7
# 4.75	4	6	8	-4	5	-4	-3	-2	6	-2	-3	-2	-2	6	9	0	-3	-1	0	8
# 5.28	-5	4	8	-3	-3	-4	6	-3	-3	0	-1	-1	-2	-3	-1	9	-3	-1	-1	10
# 5.80	5	5	-4	6	-4	-3	6	6	-3	-2	0	0	0	-2	-2	-2	0	0	-1	8
# 6.33	5	-4	-4	8	-3	-3	6	6	-2	6	-3	-3	-2	0	-3	0	-1	0	-1	-3
# 6.86	-4	-4	6	9	6	-3	6	0	-2	-3	0	-2	-1	-1	0	0	0	-1	0	9
# 7.38	-3	-3	-5	-3	-3	9	-2	6	0	-2	-1	-2	-1	-1	-1	-1	-2	0	0	12
# 7.91	-2	-2	-2	-2	-3	-2	0	-2	0	-2	-1	7	0	0	0	0	6	-2	-3	6
# 8.44	-4	5	-3	6	9	-2	-3	-1	0	0	-1	-1	0	-2	0	0	0	-1	-1	6
# 8.96	-4	-2	7	0	-2	-3	-1	-1	0	6	-2	0	0	-1	0	0	0	0	6	12
# 9.49	-4	-4	7	-2	6	6	6	-2	-1	-2	0	0	0	0	0	0	-1	0	0	6
# 10.02	12	17	15	12	15	13	9	10	10	13	12	5	5	-4	-5	10	8	-4	6	15


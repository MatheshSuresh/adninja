//#applications
#include<stdio.h>
#include<cstring>
//#include<fstream.h>
#include<stdlib.h>
#include"itoa.h"
main(){
FILE *fp;
char ch,filename[20];
int a=1,b,nfiles;
printf("enter the no of files");
scanf("%d",&nfiles);
FILE *files[nfiles];
for (int i = 1; i <= nfiles; i++)
{
	fp=fopen("strauss.ino","r");
    //printf("enter the file name");
   	//scanf("%s",&filename);
   	itoa(i,filename,10);
   	strcat(filename,".txt");
    files[i] = fopen(filename, "w");
//ch=fgetc(fp);
while(!feof(fp))
{  // fputc(ch,files[i]);
	ch=fgetc(fp);
	if(ch=='1'){
		(int)ch;
		ch=ch+i;
		putw(ch,files[i]);}
	else
	   fputc(ch,files[i]);
}
fclose(fp);
fclose(files[i]);
//fp=fopen(filename,"r");
}
}

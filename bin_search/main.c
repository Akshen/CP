/* Binary Search */

#include <stdio.h>
int binsearch(int i,int arr[10])
{
    int min,max,mid;
    min = 0;
    max  = 9;
    while(min<=max)
        {
            mid = (max + min)/2;
            if(arr[mid]==i)
                {
                    printf("%d\n",mid);
                    break;
                }
            else if (arr[mid]>i){
                max = mid-1;
            }

            else{
                    min = mid+1;
            }
        }
}
int main()
{
int i,arr[10] = {1,2,3,4,5,6,7,8,9,10};
scanf("%d",&i);
// printf("%d\n",sizeof(arr));
binsearch(i,arr);
return 0;
}

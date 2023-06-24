/*25, 32, 40, 19, 60, 55, 22
0, 25, 32, 0, 40, 40, 19*/

#include <stdio.h>

// Function to display the array

void array_display(int * arr, int N){
    int * ptr = arr;
    
    for(int k = 0; k < N; k++) {
        printf("%d ", *(ptr + k));
    }
}

int main() {
    
    // Taking number of elements:
    
    int N;
    printf("Enter the number of integers: ");
    scanf("%d", &N);

    int arr[N];
    int new_arr[N];
    
    // Taking data from user: 
    
    printf("\nEnter the numbers: ");
    for(int l = 0; l < N; l++) {
        int temp;
        scanf("%d", &temp);
        
        if(temp >= 1 && temp <= 100) {
            arr[l] = temp;
        }
        
        else{
            printf("\nThe number is not within specified range. Try again...\n");
            l -= 1;
        }
        
    }
    
    for(int i = 0; i < N; i++) {
        int first_pointer = arr[i];
        int temp = 0;
        for(int j = 0; j < i; j++) {
            int second_pointer = arr[j];
            
            //condition 1:
            if(second_pointer < first_pointer) {
                int temp_2 = second_pointer;
                
                //condition 2: 
                if(temp_2 > temp) {
                    temp = temp_2;
                }
            }
        }
        new_arr[i] = temp;
    }
    
    array_display(new_arr, N);

}
// Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

// Follow up:

// A straight forward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?

void setZeroes(int** matrix, int matrixSize, int* matrixColSize){
    int row[matrixSize],col[*matrixColSize];
    for(int i=0;i<*matrixColSize;i++)
        col[i]=0;
    
    for(int i=0;i<matrixSize;i++)
    {
        row[i]=0;
        
        for(int j=0;j<(*matrixColSize);j++)
        {
            if(matrix[i][j]==0)
            {
                row[i]=1;
                col[j]=1;
                printf("%d%d",i,j);
            }
           
        }
    }
    for(int i=0;i<matrixSize;i++)
    {
        for(int j=0;j<(*matrixColSize);j++)
        {
            if(row[i]==1||col[j]==1)
            {
                matrix[i][j]=0;
                                printf("%d%d\n",i,j);

            }
        }
    }
    return matrix;

}

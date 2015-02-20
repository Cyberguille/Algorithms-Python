
int Median_Partition(int [] A,int p,int r)
{
	int middle=0;
	if(A.Lenght()%2 !=0)		//The array is odd lenght
	int middle=(A.lenght()/2);
	else middle=(A.lenght()/2)-1;
	int pivot;
	
	if((A[l]<A[middle])&&(A[middle]<A[r]))
	{
		pivot =A[r];
		A[r]=A[middle];
		A[middle]=pivot;
	}
	else if((A[l]>A[middle])&&(A[l]<A[r]))
	{
		pivot =A[r];
		A[r]=A[l];
		A[l]=pivot;
	}
	
	return Partition (A,p,r);	
	
}

int Partition(int []A,int p,int r)
{
	int x= A[r];
	int i =p-1;
	int t;
	for(int j=p;j<r-1;j++)
	{
		if(A[j]<=x)
		{
			i++;
			t=A[i];
			A[i]=A[j];
			A[j]=t;
		}
	}
	
	t=A[i+1];
	A[i+1]=A[r];
	A[r]=t;
	return i+1;
	
}

void QuickSort(int []A,int p,int r)
{	
	int q;
	if(p<r)
	{
		q=Partition(A,p,r);
		QuickSort(A,p,q-1);
		QuickSort(A,q+1,r);
	}
}




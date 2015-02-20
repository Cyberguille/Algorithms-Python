using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace QuickSort
{
    class Program
    {
        static int Partition(int[] A, int l, int r)
        {
            int p = A[l];
            int i = l + 1;
            int t = 0;

            for (int j = i; j < r; j++)
            {
                if (A[j]<p)
                {
                    t = A[i];
                    A[i] = A[j];
                    A[j] = t;
                    i++;
                }

            }
            A[l] = A[i - 1];
            A[i - 1] = p;
            return i ;					//Este es la primera modificacion q le hize en vez de (i-1)
        }

        static void QuickSort(int []A,int l,int r)
        {
            if (l < r)
            {
                int q = Partition(A, l, r);
                QuickSort(A, l, q - 1);
                QuickSort(A, q , r);		//Esta es la 2da modificacion q en vez de q+1
            }
            
                
                
        }

        static void Main(string[] args)
        {
            /*int[] A={};
            try
            {
                using (StreamReader sr = new StreamReader("QuickSort.txt"))
                {
                    int i = 0;
                    while (!sr.EndOfStream)
                    {
                        A[i] = sr.Read();
                        i++;
                    }


                }
            }
            catch (Exception e)
            {

                Console.WriteLine("The file could not be read:");
                Console.WriteLine(e.Message);
            }
            */
           
 		    int[] A = {2,3,5,7,8,1,4,6};            
            QuickSort(A,0,A.Length);
            
            for (int i = 0; i < A.Length; i++)
            {
                System.Console.WriteLine(A[i].ToString());
            }
            System.Console.ReadLine();
        }
    }
}

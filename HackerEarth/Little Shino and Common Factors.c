#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
// Function to calculate gcd of two numbers
long long int gcd(long long int a, long long int b)
{
    if (a == 0)
        return b;
    return gcd(b%a, a);
}
 
// Function to calculate all common divisors of two given numbers 
// a, b --> input integer numbers
long long int commDiv(long long int a, long long int b)
{
    // find gcd of a,b
    long long int n = gcd(a, b);
 
    // Count divisors of n.
    long long int result = 0;
    for (int i=1; i<=sqrt(n); i++)
    {
        // if 'i' is factor of n
        if (n%i == 0)
        {
            // check if divisors are equal
            if (n/i == i)
                result += 1;
            else
                result += 2;
        }
    }
    return result;
}
 
// Driver program to run the case
int main()
{
    long long int a, b;
    scanf("%lld %lld", &a, &b);
    
    printf("%lld\n", commDiv(a, b));

    return 0;
}
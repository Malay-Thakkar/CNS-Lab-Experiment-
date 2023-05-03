#include <bits/stdc++.h>
#include <iostream>

using namespace std;


   long long int genkey(long long int primitiveroot, long long int b,
                    long long int primenum)
{
    if (b == 1)
        return primitiveroot;
 
    else
        return (((long long int)pow(primitiveroot, b)) % primenum);
}
 
// Driver program
int main()
{
    long long int primenum, primitiveroot, x, a, y, b, ka, kb;
 
    cout << "Enter value of Prime-num(Both agree) : ";
    cin>>primenum;
 
    cout << "Enter value of primitive-root(Both agree) : ";
    cin>>primitiveroot; 
//sender
    cout << "Enter private key a(Guess) : ";
    cin>>a; 
     //primitiveroot^a mod(primenum)--public key x
    x = genkey(primitiveroot,a,primenum );
 
//reciver
    cout << "Enter private key b (Guess): ";
    cin>>b;
    //primitiveroot^a mod(primenum)--public key x
    y = genkey(primitiveroot, b, primenum);
 
// exchange genreted key
    ka = genkey(y, a, primenum); 
    kb = genkey(x, b, primenum); 
    
    cout << "Secret key for a is : " << ka << endl;
 
    cout << "Secret key for b is : " << kb << endl;
 
    return 0;
}

// Exercitii.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "n=";
    cin >> n;
    cout << "8.1.1"<<endl <<"n*8="<<n*8<< endl; 
    cout << "8.1.2" << endl;
    cout <<"Catul impartirii lui n la 4 este "<<n / 4 << endl;
    cout <<"8.1.3"<<endl<<"n*10="<< (n << 2 << 1) + (n << 1) << endl;
    cout << "8.2" << endl;
    if ((n & 1) == 0) 
        cout << "Numar par";
    else
        cout << "Numar impar";
    cout << endl;
    cout << "8.3" << endl;
    int x;
    cout << "x=";cin >> x;
    cout << "n="; cin >> n;
    bool bit = x & (1 << n);
    cout << bit<<endl;
    cout << "8.4.1" << endl;
    cout << " Numarul x in care se setează bitul numarul n la valoarea 0: " << (x & (255 ^ (1 << n))) << endl;
    cout << "8.4.2" << endl;
    cout << "Numarul x in care se setează bitul n la valoarea 1: " << (x | (1 << n)) << endl;
    cout << "8.4.3" << endl;
    cout << " Numarul x in care se sterge bitul n: " << (x & ~(1 << n));
    cout << endl << "8.4.4" << endl;
    cout << "Numarul x in care se complementeaza bitul n: " << (x ^ 1 << n) << endl;
    cout << "8.5.1" << endl;
    int y;
    cout << "x="; cin >> x;
    cout << "y="; cin >> y;
    x = x + y;
    y = x - y;
    x = x - y;
    cout << x << " " << y<<endl;
    cout << "8.5.2" << endl;
    cout << "x="; cin >> x;
    cout << "y="; cin >> y;
    x = x ^ y;
    y = x ^ y;
    x = x ^ y;
    cout << " " << x << " " << y << endl;
    cout << "8.6" << endl;
    int k;
    cout << "k="; cin >> k;
    if (n == (1<<k))
        cout << "Da";
    else
        cout << "Nu";
    cout << endl << "8.7" << endl;
    int m, p, q, r;
    cout << " se citesc numerele m, p, q, r: ";
    cin >> m >> p >> q >> r;
    m = m % (int)pow(2, r);
    p = p % (int)pow(2, q);
    p = p << r;
    m = m | p;
    cout << " noua valoare a lui p este: " << p;
    return 0;
}



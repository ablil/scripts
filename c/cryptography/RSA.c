#include <stdio.h>
#include <math.h>
#include <time.h>
#define RAND_MAX 100000
#define True 1
#define False 0

struct key {
    long long key;
    long long n;
};

int is_prime(long number){
    // return True if number prime, False otherwise
    long square_root = (long)sqrt((double)number);
    for (long i = 2; i <= square_root; i++){
        if ( number % i == 0 ){
            return False;
        }
    }
    return True;
}

long pgcd(long long a, long long b){
    // pgcd algorithm
    long pgcd = 0;
    while ( 1 ){
        pgcd = a % b;
        if (!pgcd){
            pgcd = b;
            break;
        }
        a = b;
        b = pgcd;
    }
    return pgcd;
}

void generate_keys(struct key* pub_key, struct key* priv_key){
    // generate pub/priv keys and store them on pub_key & priv_key

    srand(time(NULL));

    long p = rand() % RAND_MAX, q = rand() % RAND_MAX;
    while( pgcd(p, q) != 1 ){
        p = rand() % RAND_MAX;
        q = rand() % RAND_MAX;
    }

    long n = p * q;
    long phi = (p - 1)*(q - 1);

    puts("Generating Public key...");
    long long e = rand() % phi/2;
    while ( pgcd(phi, e) != 1 ){
        e = rand() % phi/2;
    }

    puts("Generating private key...");
    long k = 2, d = 1 + phi*k;
    while ( (1+phi*k) % e != 0){
        k++;
        d = 1 + phi*k;
    }

    // storing keys
    pub_key->key = e;
    pub_key->n = n;

    priv_key->key = d;
    priv_key->n = n;

}

int main(int argc, char *argv){
    printf("Cryptography: RSA Algorithm\n");

    struct key pub_key, priv_key;
    generate_keys(&pub_key, &priv_key);
    printf("Public key {e: %d, n: %d}\n", pub_key.key, pub_key.n);
    printf("Private key {d: %d, n: %d}\n", priv_key.key, priv_key.n);

    return 0;
}

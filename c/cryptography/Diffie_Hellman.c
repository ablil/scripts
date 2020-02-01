#include <stdio.h>
#include <time.h>
#define True 1
#define False 0

struct User {
    long long priv_key; // private key used to generate a symmetric key
    long long shared_secret_key; // this is the main key used for symmetric encryption
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

long long calc_pub_key(long long priv_key, long long primitive, long long generator){
    // calculate the public key from the secret key with primitive and generator
    return generator*priv_key % primitive;
}

long calc_shared_key(long priv_key, long long pub_key, long long primitive){
    // calculate the secret shared key with pub_key, primitive & generator
    return pub_key*priv_key % primitive;
}

void Diffie_Hellman(struct User *user1, struct User *user2, long long primitive, long long generator){

    long long user1_pub_key = calc_pub_key(user1->priv_key, primitive, generator);
    long long user2_pub_key = calc_pub_key(user2->priv_key, primitive, generator);

    // the following shared secret keys should be equals to each other
    long long user1_shared_secret_key = calc_shared_key(user1->priv_key, user1_pub_key, primitive);
    long long user2_shared_secret_key = calc_shared_key(user2->priv_key, user2_pub_key, primitive);

    user1->shared_secret_key = user1_shared_secret_key;
    user2->shared_secret_key = user2_shared_secret_key;

}
int main(int argc, char *argv){
    printf("Cryptography: Diffie Hellman\n");
    srand(time(NULL));


    struct User user1, user2;
    user1.priv_key = rand();
    user2.priv_key = rand();

    long primitive = rand();
    long generator = rand();
    Diffie_Hellman(&user1, &user2, primitive, generator);

    printf("User1: private key: %d, secret key: %d\n", user1.priv_key, user2.shared_secret_key);
    printf("User2: private key: %d, secret key: %d\n", user2.priv_key, user2.shared_secret_key);

    return 0;
}

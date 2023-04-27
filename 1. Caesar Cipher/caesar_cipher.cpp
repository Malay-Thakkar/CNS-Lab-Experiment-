#include <iostream>;
using namespace std;


string cipher_encryption(string text,int key)
{
    string result = "";

    for (int i = 0; i < text.length(); i++) {

        if (isupper(text[i]))
            result += char(int(text[i] + key - 65) % 26 + 65);

        else
            result += char(int(text[i] + key - 97) % 26 + 97);
    }

    return result;
}
string cipher_decryption(string text,int key)
{
   char ch;
      for(int i = 0; text[i] != '\0'; ++i) {
         ch = text[i];
         //decrypt for lowercase letter
         if(ch >= 'a' && ch <= 'z') {
            ch = ch - key;
            if(ch < 'a'){
               ch = ch + 'z' - 'a' + 1;
            }
            text[i] = ch;
         }
         //decrypt for uppercase letter
         else if(ch >= 'A' && ch <= 'Z') {
            ch = ch - key;
            if(ch < 'A') {
               ch = ch + 'Z' - 'A' + 1;
            }
            text[i] = ch;
         }
      }
      return text;
}

int main(){
    string simpletext="";
    string result_simpletext="";
    string ciphertext="";
    string result_ciphertext="";
    int key=0;
    cout<<"Enter simple text: ";
    cin>>simpletext;
     cout<<"Enter cipher text: ";
    cin>>ciphertext;
    cout<<"Enter key: ";
    cin>>key;
    result_ciphertext=cipher_encryption(simpletext,key);
    result_simpletext=cipher_decryption(ciphertext,key);

    cout<<"Result cipher text: "<<result_ciphertext<<endl;
    cout<<"Result simple text: "<<result_simpletext<<endl;
}
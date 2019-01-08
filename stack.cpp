#include <iostream>
using namespace std;
class stack{
  int top = 0;
  int len;
  int *arr;
  public:
  stack(int size);
  void push(int num);
  void pop();
  void show();
};
stack::stack(int size){
  len = size;
  arr = new int(len);
}
void stack::push(int num){
  arr[top] = num;
  top++;
}
void stack::pop(){
  arr[top-1] = 0;
  top--;
}
void stack::show(){
  for(int i=0;i<len;i++){
    cout<<arr[i]<<"\t";
  }
}
int main() {
  int n,size;
  int choice=1;
  cout<<"1.Push 2.Pop 3.Show 4.Exit"<<endl;
  cout<<"Enter size of array!";
  cin>>size;
  stack s1(size);
  while((choice==1) || (choice==2) || (choice==3)){
  if(choice==1){
  cout<<"Enter the element to insert";
  cin>>n;
  s1.push(n);
  }
  else if(choice==2){
    s1.pop();
  }
  else if(choice==3){
    s1.show();
  }
  else if(choice==4){
    break;
  }
  else{
    cout<<"Error";
  }
  cout<<"Enter the choice!";
  cin>>choice;
  }
  return(0);
}

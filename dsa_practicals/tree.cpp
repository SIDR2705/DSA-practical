//  *ADS Asssignment No.1
//  *
//  *C++ Program To read details of a book consists of chapters,
//  *chapters consist of sections and sections consist of
//  *subsections. Construct a tree and print the nodes.
//  *Find the time and space requirements of your method.
//  **/
# include <iostream>
# include <cstdlib>
# include <string.h>
using namespace std;
/*
 * Node Declaration
 */
struct node
{
    char label[10];
    int ch_count;
    struct node *child[10];
    //char child[10];
}*root;

/*
 * Class Declaration
 */
class BST
{
    public:
        void create_tree();  
 void display(node * r1);
     
        BST()
        {
            root = NULL;
        }
};

void BST::create_tree()
{
 int tbooks,tchapters,i,j,k;
 root = new node();
 cout<<"Enter name of book";
 cin>>root->label;
 cout<<"Enter no. of chapters in book";
 cin>>tchapters; 
 root->ch_count = tchapters;
 
    for(i=0;i<tchapters;i++)
    {
      root->child[i] = new node;
      cout<<"Enter Chapter name\n";
      cin>>root->child[i]->label;   
      cout<<"Enter no. of sections in  Chapter: ";//<<root->child[i]->label;
      cin>>root->child[i]->ch_count;


          for(j=0;j<root->child[i]->ch_count;j++)
              {
               root->child[i]->child[j] = new node;
               cout<<"Enter Section "<<j+1<<"name\n";
               cin>>root->child[i]->child[j]->label;   
            //    cout<<"Enter no. of subsections in "<<root->child[i]->child[j]->label;
            //    cin>>root->child[i]->ch_count;
              }  

    }

}


void BST::display(node * r1)
{
 int i,j,k,tchapters;
 if(r1 != NULL)
 { 
  cout<<"\n-----Book Hierarchy---"<<endl;

  cout<<"\n Book title : "<<r1->label;
  tchapters = r1->ch_count;
  for(i=0;i<tchapters;i++)
  {
  
   cout<<"\n  Chapter "<<i+1;
   cout<<" "<<r1->child[i]->label;   
    cout<<"\n Sections";
   for(j=0;j<r1->child[i]->ch_count;j++)
   {
    //cin>>r1->child[i]->child[j]->label;   
    cout<<"\n  "<<r1->child[i]->child[j]->label;
   }  

  }
 }
}


/*
 * Main Contains Menu
 */
int main()
{
    int choice;
    BST bst;
    while (1)
    {
        cout<<"-----------------"<<endl;
        cout<<"Book Tree Creation"<<endl;
        cout<<"-----------------"<<endl;
        cout<<"1.Create"<<endl;
        cout<<"2.Display"<<endl;
        cout<<"3.Quit"<<endl;
        cout<<"Enter your choice : ";
        cin>>choice;
        switch(choice)
        {
        case 1:
              bst.create_tree();
        case 2:
              bst.display(root);
            break;
        case 3:
            exit(1);
        default:
            cout<<"Wrong choice"<<endl;
        }
    }
}
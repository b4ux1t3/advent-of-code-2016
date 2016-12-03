#include "stdafx.h"
#include <iostream>
#include <map>

using namespace std;

// This is the keypad. It exists in one-dimensional space, because it doesn't need to exist in any other way. 
// Your puny three-dimensional mind wouldn't understand.
int keypad[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

// This is the finger class. It keeps track of where it is, and has methods to move it around.
class Finger {
	// The finger keeps track of everything. Including a map of the keys. And a way to traverse said keys.
	// It's a really smart finger, okay?
private:
	int* currentButton;
	int* lastButton;
	int keypad[];

	

	void setKeypad(int keypad[]) {
		
	}

public:
	void printPos() {
		cout << "The current button is " << &currentButton << endl;
	}

	

	Finger(int* keypad) {
		setKeypad(keypad);
		currentButton = keypad + 5;

	}

};

// This is the entry point. That's why it's called main. :D
int main()
{
	Finger f = Finger(keypad);

	
    return 0;
}



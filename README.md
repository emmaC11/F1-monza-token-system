# F1 Monza Token System
This application can be used by attendees of the Monza 2022 Italian Grand Prix. All food & drink needs to be purchased using tokens. This application allows attendees to create an account and add tokens to the account which they can they use at the track to purchase food & drink.

# **User Experience & Functionality**

# User Stories
* As a first time user, I want to create an account.
* As a first time user, I want to add tokens to my account.
* As a first time user, I want to withdraw tokens from my account.
* As a first time user, I want to transfer tokens to my friend.
* As a first time user, I want to search for my friend on the system.
* As a first time user, I want to view other attendees using the application.

## Diagrams
Use Case Diagram & Class Diagram developed using [Lucid Chart](https://lucid.app/lucidchart/ae7a1d80-d51b-4265-8c00-f8b68836fd6e/edit?beaconFlowId=C5E6AF6BD782FA24&invitationId=inv_38752bd1-bdde-4c7f-8d8d-eba843da0469&page=0_0#)

![image](https://user-images.githubusercontent.com/83119583/190186382-ef471d0b-9346-41c2-a67d-67e62e8f1a7b.png)

![image](https://user-images.githubusercontent.com/83119583/190193272-6e2637eb-d03e-45dd-99eb-7ec7142cb6d2.png)

# **Features**

## Main Menu
* When the application loads successfully, a main menu is displayed with a list of options that the user to select from.
* The applications title has a pink colour to distinguish it from the menu options.
* The menu options are displayed in a liit format with a number correspoding each action.
* There is an input prompt that prompts the user to enter their selection from the menu.

![image](https://user-images.githubusercontent.com/83119583/192308716-930949a8-1487-4efe-b577-64b3bcfc28b5.png)


## View Users
* Users can view other atteendees of the grand prix who are using this system.
* Menu option '1' must be selected to open the view users dialog.
* All users of the system are displayed, the information provided is: account number, first name, last name, seat number, overdraft status & token balance.
* The column headings have a blue text colour to highlight that they are headings not user details.
* The user must click the return button to return to the main menu screen

![image](https://user-images.githubusercontent.com/83119583/192310364-308b0a09-49ba-43fc-985b-b1f70438f3a6.png)


## Deposit Tokens
* Users can add tokens to their account, which they can use to buy food & drink around the track.
* Menu option '3' must be selected to open the 'add tokens' dialog.
* The user will be prompted to enter their account number & the amount of tokens they want to deposit.
* If user inputs are valid, the tokens will be added to their account & their balance will be updated.

![image](https://user-images.githubusercontent.com/83119583/192313863-308d46cc-57be-4cf5-b990-dcd348954ede.png)

## Withdraw Tokens
* Users can withdraw tokens from their account, which they can use to buy food & drink around the track.
* Menu option '4' must be selected to open the 'withdraw tokens' dialog.
* The user will be prompted to enter their account number & the amount of tokens they want to withdraw.
* Users can withdraw an amount greater than their current balance if they are signed up to the overdraft facility.
* If the user inputs are valid, the tokens will be withdrawn from their account & their balance will be updated.
* The user will be provided with a code that they can enter at the kiosks located around the track to claim their tokens.

![image](https://user-images.githubusercontent.com/83119583/192315324-1244999e-f742-4360-8664-d8a9c1da92c3.png)

## Transfer Tokens
* Users can transfer tokens from one account to another, which they can use to buy food & drink around the track.
* Menu option '5' must be selected to open the 'transfer tokens' dialog.
* The user will be prompted to enter their account number & the amount of tokens they want to transfer.
* Users can transfer an amount greater than their current balance if they are signed up to the overdraft facility.
* The user will then be prompted to enter the account number of the user they want to transfer their tokens to.
* If the user inputs are valid, the tokens will be transferred from one account to another & the token balances will be updated.

![image](https://user-images.githubusercontent.com/83119583/192317363-1749a3fb-1d11-42b6-8c04-649e1dcea4ae.png)




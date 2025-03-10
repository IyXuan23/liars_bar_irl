<template>
    <div class="masterbox">
        <div class="columnbox">
            <div class="column">
                <div class="title">About</div>
                <div class="textbox">This web app was designed to simulate the popular steam game Liar's Bar. It
                    is designed with 4 players in mind, and currently only has 1 lobby for use for me and my friends. 
                    If you chance upon this site by random, congratulations I don't know how you did it.
                </div>
            </div>
            <div class="column">
                <div class="title">Instructions</div>
                <div class="textbox">
                    On the homepage click the [Join Game] button, then click the [Ready] button to ready up. 
                    Game will automatically start when all players are ready
                </div>
            </div>
        </div>
        <div class="rules">
            <div class="title">
                Rules
            </div>
            <div class="textbox">
                <ul>
                    <li>Each player starts with a Revolver with 6 chambers, and 1 bullet in a random chamber</li>
                    <li>Every round, a card type will be announced (King, Queen, Ace), and each player dealt 5 cards</li>
                    <li>Only cards of that type can be played during this round</li>
                    <li>The current player can choose to either call out the cards of the previous player, 
                        or play a number of cards from their own hand</li>
                    <li>If you are caught playing the wrong cards, you pull the trigger once. Otherwise, the player who 
                        made the false claim pulls the trigger
                    </li>
                    <li>ie. This whole game is a game of bluff, whether you can play the wrong cards and not get called</li>
                    <li>NOTE: Jokers count as all card types</li>
                </ul>
            </div>
        </div>
        <div class="buttonbox">
            <button class="back" onclick="window.location.href = '/'">Back</button>
        </div>
    </div>
</template>

<style scoped>

.masterbox {
    display: flex;
    flex-direction: column;
    gap: 32px;
    width: 80vw;
}

.columnbox {
    display: flex;
    flex-direction: row;
    gap: 32px;
    width: 100%;
}

.column {
    flex: 1;
    justify-content: center;
    align-items: center;
}

.title {
    text-align: center;
    font-size: 32px;
    padding: 4px;
    background-color: darkslategrey;

}

.textbox {
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 4px;
    padding-right: 4px;
}

.back{
    background-color: lightgray;
    font-size: 16px;
    border-radius: 6px;
    padding-top: 4px;
    padding-bottom: 4px;
    padding-left: 8px;
    padding-right: 8px;
    border: none;
}

.back:hover{
    background-color: gray;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    cursor: pointer;
}
</style>
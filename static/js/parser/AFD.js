
class FiniteAutomataParser {
    constructor() {
        this.currentState = "ExpectingType";
        this.finalState = "F";
        this.keywords = {
            dataTypes: ["Integer", "Real", "Character", "String"],
            delimiters: {
                openers: ['(', '[', '{'],
                closesrs: [')', ']']
            }
        };

        this.currentDT = null;
        this.currentLit = null;
        this.currentOpener = null;
        this.currentCloser = null;
        this.currentValues = [];
        this.results = [];
    }
}
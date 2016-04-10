var raspi = require('raspi-io');
var five = require('johnny-five');
var board = new five.Board({
  io: new raspi()
});


board.on("ready", function() {

  var lcd = new five.LCD({
    controller: "PCF8574"
  });

  lcd.useChar("heart");

  lcd.cursor(0, 0).print("hello :heart:");

  lcd.blink();

  lcd.cursor(1, 0).print("Blinking? ");
});
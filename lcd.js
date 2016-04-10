Cylon = require('cylon');

Cylon.robot({
  connections: {
    raspi: { adaptor: 'raspi' }
  },

  devices: {
    lcd: { driver: 'lcd' }
  },

  work: function(my) {
    my.lcd.on('start', function(){
      my.lcd.print("Hello!");
    });
  }

}).start()

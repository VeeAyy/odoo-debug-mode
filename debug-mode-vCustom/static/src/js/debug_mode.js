odoo.define('debugmode', function (require) {
"use strict";


var Widget = require('web.Widget');
var SystrayMenu = require('web.SystrayMenu');

    var DebugMode = Widget.extend({
        template:'Icon',
    });

    DebugMode.prototype.sequence = 10;
    SystrayMenu.Items.push(DebugMode);
});
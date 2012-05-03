/**
 * Your Javascript code goes here.
 *
 * This file is deployed as ++resource++youraddon/main.js on your site 
 * and automatically included in merge bundles via jsregistry.xml.
 *
 * More info
 *
 * http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/javascript.html
 *
 */

 /*global window,document*/

(function($) {
     
     "use strict";


     $(document).ready(function() {

        // Page has been loaded, put your custom JS logic here

        // EXAMPLES START
        // Example how to manipulate my-custom-footer viewlet
        // and install a click handler via jQuery
        $(".my-footer-viewlet").click(function() {
                window.alert("Greetings from Finland");
        });
        // EXAMPLES END
     });

})(jQuery);


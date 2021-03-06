﻿// Handles all the controller logic for the awards page
$(function() {

var awardsElm = $('.awards-content');
var listElm = $('.list-widget');

var awardElm = $('.award-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the award identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual award screen
         awardsElm.hide();
         awardElm.show();
         $.mgr.requestAward(id);
      } else {

         // Show the awards list screen
         awardElm.hide();
         awardsElm.show();
         $.mgr.requestAwards();
      }
   },

   requestAwards: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/awards/index.json',
         dataType: 'json',
         success: $.proxy($.mgr.onAwards, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected award
      $.ajax(options);
   },

   requestAward: function(id) {

      // Display the loading indicator
      tableElm.table({ showAll: true });
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/awards/' + id + '.json',
         dataType: 'json',
         success: $.proxy($.mgr.onAward, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected award
      $.ajax(options);
   },

   onAwards: function(data) {

      // Update the header
      var headerElm = $('.common-header', awardsElm);
      headerElm.text('Awards (' + data.length + ')');

      // Populate the list with awards
      listElm.list('setRows', data);
   },

   onAward: function(data) {

      // Update the header
      var headerElm = $('.common-header-title', awardElm);
      headerElm.text(data.name);

      // Update the navigation buttons
      var prevElm = $('.award-nav-prev', awardElm).button(
            { icons: { primary: 'ui-icon-circle-arrow-w' }, text: false });
      if (data.prev_id) {
         prevElm.attr('href', '#id=' + data.prev_id);
         prevElm.button({ disabled: false });
      } else {
         prevElm.button({ disabled: true });
      }
      var nextElm = $('.award-nav-next', awardElm).button(
            { icons: { primary: 'ui-icon-circle-arrow-e' }, text: false });
      if (data.next_id) {
         nextElm.attr('href', '#id=' + data.next_id);
         nextElm.show();
      } else {
         nextElm.hide();
      }

      // Update the award attributes
      $('.award-desc', awardElm).text(data.desc);

      // Populate the table with award results
      tableElm.table('setColumns', data.columns);
      tableElm.table('setRows', data.rows);
   },

   onError: function(request, status, error) {
   
   }

}});

// Callback when the URL fragment changes
$(window).on('hashchange', $.mgr.onHistory);

// Load the custom jQuery user interface components
$('.common-nav').nav();

// Trigger the history event on initial page load
$(window).trigger('hashchange');

});

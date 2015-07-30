#!usr/bin/env python

from zope.testbrowser.browser import Browser
from zope.testbrowser import interfaces
from zope.interface.verify import verifyObject
import urllib

browser = Browser()
browser.raiseHttpErrors = False
#browser.handleErrors =  False

print browser
try:
    browser.open("https://750words.com/auth",)
except ValueError:
    pass
browser.url
browser.headers

email = 'rpvnwnkl@gmail.com'
password = 'password'

signIn = browser.getForm(id='signin_form')
emailEnter = signIn.getControl(name='person[email_address]')
passwordEnter =  signIn.getControl(name='person[password]')

emailEnter.value = email
passwordEnter.value = password

signIn.submit()

print browser.url
print browser.headers

form = browser.getForm()

words = open('entrytext.txt', 'r').read()
entry_id = form.getControl(name='entry[id]').value
print entry_id

num_words = str(len(words))
print words
body = words
verify_success = 'ctrls'
entry_record_version = '1'

form.getControl(name='changed').value = '1'
form.getControl(name='words_at_last_save').value = '0'
form.getControl(name='words_at_last_autosave').value = '0'
form.getControl(name='country').value = 'USA'
form.getControl(name='entry[id]').value = entry_id
form.getControl(name='entry[num_words]').value = num_words
form.getControl(name='entry[record_version]').value = '1'
form.getControl(name='entry[body]').value = body
print browser.contents
#form.submit()
data1 = 'entry[id]=4876827&entry[num_words]=5&entry[body]=hello%20mudda%20fadda%20grandma%20adda&v=ctrls&rv=13'
data = "window.onbeforeunload = function (e) {  e = e || window.event;  if ($('#changed').val() == 0) {    // No change leaving the page is ok.    return;  }  // IE, Firefox prior to v 4.  if (e) {    e.returnValue = 'Ahoj!';  }  // Safari  return 'Ahoj!';};var check_outbound_links = true;function autosave(verify_success, continue_to_url) {   var entry_id  = $('#entry_id').val();  var body      = encodeURIComponent($('#entry_body').val());   var num_words = $('#entry_num_words').val();   var num_words_at_last_autosave = $('#words_at_last_autosave').val();  var new_words = num_words - num_words_at_last_autosave;  var changed   = $('#changed').val();  if (verify_success != 'losing_words_is_okay' && new_words < -30) {     $('#losing_words').html('Uh oh!  My records show that your entry used to be longer than it currently is.  It used to be '+num_words_at_last_autosave+' words, but is now '+num_words+' words... therefore losing '+(-new_words)+' words.  To revert, cancel this box and reload this page.');      $('#losing_words').dialog({           bgiframe: true,           resizable: false,           height:250,           modal: true,           overlay: {              backgroundColor: '#000',              opacity: 0.5           },           buttons: {              'Save anyway': function() {                  $(this).dialog('close');                  autosave('losing_words_is_okay');               },               Cancel: function() {                   $(this).dialog('close');               }            }      });      $('#losing_words').dialog('open');  } else {      if (changed == '1' || verify_success == 'losing_words_is_okay') {          $('#save_message').html('Saving');          $('#autosaving_indication').removeClass('not-saved').removeClass('saved');          var img = document.createElement('IMG');          img.src = '/images/dots-white.gif';          document.getElementById('autosaving_indication').appendChild(img);          $.ajax({               type: 'POST',               url: '/autosave',               data: 'entry[id]=' + entry_id + '&entry[num_words]=' + num_words + '&entry[body]=' + body + '&v=' + verify_success + '&rv=' + $('#entry_record_version').val(),               dataType: 'script',              cache: false,               success: function(message) {                  var nv = $('#entry_num_words').val();                  var sw = $('#words_at_last_autosave').val();                  if((nv-sw)>0) {                    $('#changed').val('1');                    $('#autosaving_indication').html("").removeClass('saved').addClass('not-saved');                  } else {                    $('#changed').val('0');                  }                  if (verify_success == 'ctrls') {                      $.achtung({message: 'Force-saved it. Continue on!',                                  timeout:5,                                  icon: 'ui-icon-check',                                 className: 'achtungSuccess'});                  } else if (verify_success == 'losing_words_is_okay') {                      $.achtung({message: 'Saved it!',                                  timeout:5,                                  icon: 'ui-icon-check',                                 className: 'achtungSuccess'});                  } else if (continue_to_url) {                      window.location = continue_to_url;                  }              },              error: function(message, ajaxOptions, thrownError) {                  $('#changed').val('1');                  $('#save_message').html('Error saving.');                  $.achtung({message: 'Error autosaving entry. Make sure your words are saved before continuing.',                              timeout:5,                              icon: 'ui-icon-alert',                             className: 'achtungFail'});              }          });      }  }  // To prevent another thread running set timeout only   // when we do not call autosave() from within autosave().  var s;  if (verify_success != 'losing_words_is_okay') {    s = setTimeout(autosave, 35000);  }  return false;};$(document).ready(function(){    $('#entry_body').simplyCountable({        counter: '#counter',        hiddenField: '#entry_num_words',        countType: 'words',        maxCount: 750,        strictMax: false,        countDirection: 'up',        safeClass: 'wordcount_under',        overClass: 'wordcount_over',        thousandSeparator: ','    });            $('textarea').tabby();    $('#entry_body').autoResize({        // On resize:        onResize : function() {            if ($('#entry_body')[0].selectionStart == $('#entry_body').val().length) {                                $.scrollTo('#footer', 0);                            }        },        // After resize:        animateCallback : function() {        },        // Quite slow animation:        animateDuration : 0,        // More extra space:         extraSpace : 40,        // Limit to how big the text area can get. Effectively no limit.        limit : 1000000    }).trigger('change');            $('#entry_body').focus();    $('#entry_body').val($('#entry_body').val()+'\n');    $('#entry_body').val($('#entry_body').val().substr(0,$('#entry_body').val().length - 1));    $.scrollTo('#footer', 400, {});    $('#entry_body').keyup(needsSaving);        function needsSaving() {        var changed = $('#changed').val();        if (changed == '0') {            $('#changed').val('1');            $('#autosaving_indication').html('').removeClass('saved').addClass('not-saved');        }        if ($('#seconds_left').length > 0) {            $('#seconds_left').val(600);        }    }            autosave();        $(document).bind('keydown', function(event) {        if ((event.which == 115 || event.which == 83) && (event.ctrlKey || event.metaKey)) {                      $('#changed').val('1');            autosave('ctrls');            event.stopPropagation();              event.preventDefault();            return false;                  } else {          bindOutboundLinks();        }        return true;    });//   Redundant. See $(document).bind('keydown'..//    $(window).keypress(function(event) {//       bindOutboundLinks();//       return true;//    });        function bindOutboundLinks() {        $('a').click(function(event) {            // Do not autosave when making xhr request.            if ($(this).attr('id') == 'aes' || $(this).attr('id') == 'asl' || $(this).attr('id') == 'header-controll') {              return true;            };            var c = $('#changed').val();            var b = $('#entry_body').val();            if (check_outbound_links != false && c == '1' && b.length > 0) {                check_outbound_links = false;                $.achtung({message: 'Saving your entry before you go.',                           timeout:5,                           icon: 'ui-icon-check',                           className: 'achtungSuccess'});                autosave('go_to_stats', $(this).attr('href'));                event.preventDefault();                return false;            }        });    }    checkPace();    function checkPace() {        var entry_id  = $('#entry_id').val();        var num_words = $('#entry_num_words').val().replace(/,/g,'');         var words_at_last_save = $('#words_at_last_save').val();         if (num_words != words_at_last_save) {            var new_words = num_words - words_at_last_save;            $.ajax({                 type: 'POST',                 url: '/pace',                 data: 'entry[id]=' + entry_id + '&new_words=' + new_words + '&total_words=' + num_words,                 cache: false,                 success: function(message) {},                error: function(message) {                    $('#words_at_last_save').val(words_at_last_save);                }            });        }        var t = setTimeout(checkPace, 60000);     }    if (google.loader.ClientLocation && $('#country').val() == '') {      var loc = google.loader.ClientLocation;      $.ajax({           type: 'POST',            url: '/locate',           data: 'country=' + encodeURIComponent(loc.address.country) + '&region=' + encodeURIComponent(loc.address.region) + '&city=' + encodeURIComponent(loc.address.city) + '&lat=' + loc.latitude + '&lng=' +loc.longitude,          cache: false,        success: function(message) {             $('#country').val(loc.address.country);         },         error: function(message) {}      });    }    $('#header-controll').click(function(e) {      var hc = this;      e.preventDefault();      $('#header').toggle('slow');      $('#bowling-score-tally').toggle('slow', function() {        if ($(this).css('display') === 'none') {           $('span', hc).text('+');        } else {           $('span', hc).text('-');            }      });    });  $('#months_progress img').bt({     fill: '#F4F4F4',     strokeStyle: '#666666',      spikeLength: 20,     width: 200,     spikeGirth: 10,     overlap: 0,     centerPointY: 1,     cornerRadius: 0,      cssStyles: {       fontFamily: ''Lucida Grande',Helvetica,Arial,Verdana,sans-serif',        fontSize: '12px',       padding: '10px 14px'     },     shadow: true,     shadowColor: 'rgba(0,0,0,.5)',     shadowBlur: 8,     shadowOffsetX: 4,     shadowOffsetY: 4  });});"
dataparam = 'entry[id]=', entry_id, ', entry[num_words]=',num_words, \
            ', entry[body]=',body,', v=', verify_success, \
                               ', rv=entry_record_version'

dataparams = "{'entry[id]':entry_id, \
                               'entry[num_words]': num_words, \
             'entry[body]': body, 'v':verify_success, 'rv':entry_record_version}"

dataprams = "entry[id]=" + entry_id + "&entry[num_words]=" + num_words \
             + "&entry[body]=" + body + "&v=" + verify_success + "&rv=" \
             + entry_record_version
browser.post('/autosave', dataparams, 'script')
#browser.post('http://750words.com/autosave', dataparams, 'script')








/* global Recorder, FormData, location, XMLHttpRequest */

const fileType = 'video' // or "audio"
const fileName = `${new Date().toISOString()}.wav`

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


const xhr = (url, data, callback) => {
  var request = new XMLHttpRequest()
  request.onreadystatechange = function () {
    console.warn(request)
    if (request.status === 200) {
      return callback(null, location.href + request.responseText)
    } else {
        callback(new Error('Fail file upload'))
    }
  }
  request.open('POST', url)
  request.send(data)
}

const sendFile = (url, blob, callback) => {
  var formData = new FormData()
  formData.append('name', fileName)
  formData.append('file', blob)
  formData.append('csrfmiddlewaretoken', csrftoken)

  xhr(url, formData, callback)
}

function getAudioContext () {
  try {
    // webkit shim
    var AudioContext = window.AudioContext = window.AudioContext || window.webkitAudioContext
    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia
    window.URL = window.URL || window.webkitURL
    return new AudioContext()
  } catch (error) {
    console.error(error)
    return null
  }
}

var config = {audio: true}
var logError = function (error) { console.error(error) }

var recorder
function AudioRecord (onFinish) {
  var audioContext = getAudioContext()

  if (audioContext === null) {
    throw new Error('Not support WebAudioAPI')
  }

  function loadMedia (stream) {
    var input = audioContext.createMediaStreamSource(stream)
    recorder = new Recorder(input)
  }

  navigator.getUserMedia(config, loadMedia, logError)

  function start () {
    recorder.record()
  }

  function stop () {
    recorder.stop()
    recorder.exportWAV(function (blob) {
      onFinish && onFinish(blob)
      recorder.clear()
    })
  }

  return {
    start: start,
    stop: stop,
    save: sendFile
  }
}

window.AudioRecord = AudioRecord
window.sendFile = sendFile

/* global AudioRecord, sendFile, URL */


var control = document.querySelector('#control')
var list = document.querySelector('#recordingslist')
var icon = document.querySelector('.icon')
var URL_POST = '/materia/1/'
var record

function changeEvent (one, two) {
  control.removeEventListener('click', one)
  control.addEventListener('click', two, false)
}

function onPlay () {
  record.start()
  icon.classList.remove('fa-microphone')
  icon.classList.add('fa-stop', 'active')
  changeEvent(onPlay, onStop)
}

function onStop () {
  record.stop()
  icon.classList.remove('fa-stop', 'active')
  icon.classList.add('fa-microphone')
  changeEvent(onStop, null)
}

function createPlayer (blob) {
  location.reload()
  // var url = URL.createObjectURL(blob)
  // var audio = document.createElement('audio')
  //
  // audio.controls = true
  // audio.src = url
  // list.appendChild(audio)
}

function setDefultAction (error, data) {

  icon.classList.remove('fa-refresh', 'fa-spin')
  icon.classList.add('fa-microphone')
  control.addEventListener('click', onPlay, false)
}

function onFinish (blob) {
  createPlayer(blob)
  icon.classList.remove('fa-microphone', 'active')
  icon.classList.add('fa-refresh', 'fa-spin')
  sendFile(URL_POST, blob, setDefultAction)
}

record = AudioRecord(onFinish)
control.addEventListener('click', onPlay, false)

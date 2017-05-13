<template>
  <div id="app">
    <Board url="http://127.0.0.1:8000/api/boards/1/"></Board>
  </div>
</template>

<script>
import Board from './components/Board'

export default {
  name: 'app',
  components: {
    Board
  },
  data: function () {
    return{
      boards:{}
    }
  },
  methods:{

  },
}
</script>

<style>
  html, body {
    display: flex;
    flex-direction: column;
    height: 100%;
    margin: 0;
    padding: 0;
  }
  #app {
    display: flex;
    flex: 1 1 100%;
  }
</style>

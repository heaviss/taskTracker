<template>
  <div class="board">
    <header >
      <h3>{{board.name}}</h3>
    </header>

    <div class="row">
      <List v-for="list in board.lists" :url="list" :key="list.url"></List>
      <div class="col-md-4">
        <form class="addNew" v-on:submit="addNewList">
          <input class="newText" type="text" v-model="newListName" placeholder="New list name">
          <input type="submit" value="Add">
        </form>
      </div>
    </div>
    <footer>Сделал Вова Серёгин. <a href="https://github.com/heaviss/taskTracker">Репозиторий на гитхабе</a></footer>
  </div>
</template>

<script>

import List from './List'

export default {
  name: 'Board',
  components: {List},
  props: ['url'],
  data: function () {
    return {
      board: "",

      newListName: ""
    }
  },
  methods:{
    getBoard: function() {
      this.$http.get(this.url)
        .then(responce => {
          this.board = responce.body
        })
    },
    addNewList: function (txt) {
        alert("addNewList called. Implement it!");
        txt.preventDefault();
    }
  },
  created: function() {
    this.getBoard()
  }
}
</script>

<style>
  ul {
    list-style-type: none;
    padding-left: 0;
    margin: 1em;
  }
  .row{
     /* white-space: nowrap;*/

      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      flex: 1 1 100%;
      overflow-x: auto;
  }

  .row .col-md-5, .col-md-4{
      border: 6px;
      margin-right: 1em;
      margin-left: 1em;
      flex-grow: 1;
  }
  .row .col-md-5{
    min-width: 350px;
    flex-basis: 350px;
  }

  .row .col-md-4 {
    min-width: 18em;
    flex-basis: 300px;
    border-radius: 1px;
  }

  .addNew {
    display: flex;
    flex-grow: 1;
    border: 1px solid #bc8dd8;
  }
  .addNew .newText {
    flex-grow: 1;
  }
  .board {
    display: flex;
    height: 100%;
    flex-direction: column;
    background-color: #d3b2e6;
  }
  header {
    flex: 0 0 auto;
    background-color: #bc8dd8;
    margin: 0 0 1em 0 ;

  }
  header h3 {
    padding-left: 1em;
  }
  footer {
    flex: 0 0 auto;
    background-color: #bc8dd8;
    margin-top: 1em;
    font-size: 0.9em;
  }
</style>

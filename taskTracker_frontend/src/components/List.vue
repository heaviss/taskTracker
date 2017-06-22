<template>
  <div class="list col-md-4" >
    <header>
      <strong>{{list.name|capitalize}}</strong>
    </header>

    <ul>
      <li v-for="task in notArchived(list.projects)" :key="task.url">
        <Task v-on:archivate="getList" :url="task.url"></Task>
      </li>
    </ul>
    <ul>
      <li v-for="task in notArchived(list.tasks)" :key="task.url">
        <Task v-on:archivate="getList" :url="task.url"></Task>
      </li>
    </ul>
    <ul>
      <li v-for="task in notArchived(list.subtasks)" :key="task.url">
        <Task v-on:archivate="getList" :url="task.url"></Task>
      </li>
    </ul>

    <footer>
      <form class="addNew" v-on:submit="addNewTask">
        <input class="newText" type="text" v-model="newTaskName" placeholder="Новая задача">
        <input type="submit" value="Add">
      </form>
    </footer>
  </div>
</template>

<script>

import Task from './Task'

export default {
  name: 'List',
  components: {Task},
  props: ['url'],
  data () {
    return {
      newTaskName : "",

      list: {}
    }
  },
  methods:{
    addNewTask (txt) {
      txt.preventDefault();

      if (this.newTaskName) {
        let newTask = {
          "name": this.newTaskName,
          "description": "",
          "status": "A",
          "parent_project": null,
          "owner_list": this.url,
          "subtasks": [],
          "attachments": []
        };
        //construct url for POST
        let url = this.url.slice(0, this.url.indexOf("api")+4)+"tasks/";
        this.$http.post(url,newTask)
          .then(responce => {
            if (~responce.status.toString().indexOf("20")) {
              this.list.tasks.push(responce.body);
              //console.log(responce.status)
              this.newTaskName = ""
            }
            else {
              console.log(responce.body)
            }
          })
      }
    },

    getList: function() {
      this.$http.get(this.url)
        .then(responce => {
          //this.name = responce.body["name"]
          this.list = responce.body
    //  console.log(this.list.tasks.filter( task => {this.status != "D"}))
        })
    },

    notArchived: function (tasks) {
      if (tasks) {
        return tasks.filter( function (task) {
            return ("status" in task && task.status !== "D")
          }
        )
      }
    }
  },

  filters: {
    capitalize: function (value) {
      if (!value) return '';
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  created: function() {
    this.getList()
  }

}
</script>

<style scoped>
  .list {
    background: #bc8dd8;
  }
  header {
    margin: 1em;
    font-size: 14pt
  }
  li {
    margin-bottom: 0.5em
  }
</style>

<template>
  <div class="list">
    <header @click="showDetails=true">{{content.name}}</header>

    <transition v-if="showDetails" name="modal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div v-on-clickaway="saveAndClose" class="modal-container">

            <input type="text" v-model="newContent.name" class="header"/>

            <textarea type="text" v-model="newContent.description"></textarea>
            <input type="button" @click="archivateTask" value="Сделано!"/>
            <div class="modal-footer">
              <button class="modal-default-button" @click="saveAndClose">
                Сохранить
              </button>
              <input type="button" @click="discardAndClose" value="Закрыть"/>
            </div>
          </div>
        </div>
      </div>
    </transition>

    <footer>

    </footer>
  </div>
</template>

<script>

  import {mixin as clickaway} from 'vue-clickaway';

  export default {
    name: 'Task',
    props: ['url'],
    computed: {},
    mixins: [clickaway],

    data () {
      return {
        content: {},
        showDetails: false,
        newContent: {}
      }
    },

    methods: {
      getContent: function () {
        this.$http.get(this.url)
          .then(responce => {
            this.content = responce.body;
            for (let key in this.content) {
              this.newContent[key] = this.content[key]
            }
          })
      },

      updateTask: function () {
        if (this.isUpdated()) {
          this.$http.put(this.url, this.newContent)
            .then(responce => {
              console.log("Обновлено: " + this.content.name)
            })
        }
      },

      archivateTask: function () {
        console.log(this.newContent.status !== this.content.status);
        this.newContent.status = "D";
        console.log(this.newContent.status !== this.content.status);
        this.updateTask();
        this.$emit('archivate')//, this.newContent.name)
      },

      saveAndClose: function () {
        this.updateTask();
        this.showDetails = false
      },

      discardAndClose: function () {
        for (let key in this.content) {
          this.newContent[key] = this.content[key]
        }
        this.showDetails = false
      },

      isUpdated: function () {
        //let fields = ["attachments", "description", "name", "owner_list", "status", "subtasks", "url"]
        return (this.newContent.description !== this.content.description ||
        this.newContent.name !== this.content.name ||
        this.newContent.status !== this.content.status)
      }
    },

    created: function () {
      this.getContent()
    }
  }
</script>

<style scoped>

  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    display: table;
    transition: opacity .3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 300px;
    margin: 0 auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;

    display: flex;
    flex-direction: column;
  }

  /*
   * The following styles are auto-applied to elements with
   * transition="modal" when their visibility is toggled
   * by Vue.js.
   *
   * You can easily play with the modal transition by editing
   * these styles.
   */

  .modal-enter .modal-container,
  .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }

  .modal-footer {
    display: flex;
    justify-content: space-between;
  }

  .header {
    font-size: 18px;
  }
</style>

<template>
  <div id="app" class="container">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading">Users</h3>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Avatar</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in all_users" v-bind:key="user">
            <td>{{ user.id }}</td>
            <td><img v-bind:src="user.avatar" width="50"/></td>
            <td>{{ user.first_name + " " + user.last_name }}</td>
            <td>{{ user.email }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'app',
  data () {
    return {
      loading: false,
      all_users: null
    }
  },
  mounted () {
    this.loading = true;
    axios
      .get('https://reqres.in/api/users?page=1')
      .then(response => (this.all_users = response.data.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
  }
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
.heading {
  margin-bottom: 30px;
}
</style>
<template>
  <div id="app" class="container">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading" style="text-align:left">Patients</h3>
      <input  v-model = "searchstring" placeholder ="Search here">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
           
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in all_patients" v-bind:key="patient">
            <td>{{ patient.id }}</td>
            <td>{{ patient.first_name + " " + patient.last_name }}</td>
            <td>{{ patient.email }}</td>
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
      all_patients: null
    }
  },
  mounted () {
    this.loading = true;
    axios
      .get('http://localhost:8000/Patients/?format=json')
      .then(response => (this.all_patients = response.data))
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
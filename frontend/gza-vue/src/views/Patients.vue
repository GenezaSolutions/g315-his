<template>
  <div id="PatientList" class="container">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h3 class="heading" style="text-align:left">Patients List</h3>
      <input id="lens" v-model= "search" placeholder ="Search here">
      <br></br>


      
  </div>


      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Mobile</th>
            <th scope="col">Email</th>
            <th>Details</th>
          
           
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in filteredPatients" v-bind:key="patient">
            <td><router-link :to="{name: 'patientdetail', params: { id: patient.id}}">{{ patient.id }}</router-link></td>
            <td>{{ patient.first_name + " " + patient.last_name }}</td>
            <td>{{ patient.mobile }}</td>
            <td>{{ patient.email }}</td>
            <td><router-link :to="{name: 'patientdetail', params: { id: patient.id}}">></router-link></td>
          </tr>
        </tbody>
      </table>



   
    </div>

   
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'PatientList',
  data () {
    return {
      loading: false,
      patients: '',
      search: '',
      
    }
  },
  mounted () {
    this.loading = true;
    axios
      .get('http://localhost:8000/Patients/?format=json')
      .then(response => (this.patients = response.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
      
  },




computed: {
    filteredPatients() {
      return this.patients.filter(patient => {
       return `${patient.first_name} ${patient.last_name} ${patient.email} ${patient.mobile} ${patient.id}`.includes(this.search);
     
    })
  }
//ALTERNATE METHOD TO EXPLORE
//filteredPatients: function(search, patients) {
//    const terms = search.toLowercase()
//    return patients.filter(patient => {
//        return patient.first_name.toLowercase().indexOf(terms) >= 0 || patient.last_name.toLowercase().indexOf(terms) >= 0
//    })
//

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

#lens {

position: relative;
left: -468px;
}
 
</style>
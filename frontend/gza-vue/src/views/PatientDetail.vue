<template>
  <div id="PatientList" class="container">
    
    <div>
      <h3 class="heading" style="text-align:left">ID {{$route.params.id}}</h3>
      <input id="lens" v-model= "search" placeholder ="Search here">
      <br><br>


      
  </div>


      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Mobile</th>
            <th scope="col">Email</th>
            
          
           
          </tr>
        </thead>
        <tbody>
          <tr v-bind:key="patient">
            <td>{{ patient.id }}</td>
            <td>{{ patient.first_name + " " + patient.last_name }}</td>
            <td>{{ patient.mobile }}</td>
            <td>{{ patient.email }}</td>
            <td>></td>
          </tr>
        </tbody>
      </table>



   
    </div>

   
  
</template>

<script>
import axios from "axios";
export default {
  name: 'PatientList',
  data () {
    return {
      
      patient: '',
      
      
      
      
    }
  },
  mounted () {
    
    
    axios
      .get('http://localhost:8000/Patients/'+ this.$route.params.id +'/?format=json')
      .then(response => (this.patient = Object.assign({}, this.patient, response.data)))
      .catch(error => console.log(error))
     
      
  },
 
 watch: {
  '$route.params.id' () {

    axios
      .get('http://localhost:8000/Patients/'+ this.$route.params.id +'/?format=json')
      .then(response => (this.patient = Object.assign({}, this.patient, response.data)))
      .catch(error => console.log(error))
     
      
    // reload the data here
  }
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
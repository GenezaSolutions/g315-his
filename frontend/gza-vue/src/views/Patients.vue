<template>
  <div class="patients">
    <PatientList msg="Patients Record" />
  </div>
</template>

<script>
// @ is an alias to /src
import PatientList from "@/components/PatientList.vue";

export default {
  name: "patients",
  components: {
    PatientList
  }
};
</script>

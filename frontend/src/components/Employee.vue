<template>
  <el-table :data="tableData" width="100%">
    <el-table-column prop="name" label="名字"></el-table-column>
    <el-table-column prop="department" label="部门"></el-table-column>
  </el-table>
</template>
<style>
</style>
<script>
import Axios from "axios";
export default {
  data() {
    return {
      tableData: [],
    };
  },
  mounted() {
    Axios.get(this.GLOBAL.baseUrl + "employee/").then((res) => {
      console.log(res.data);
      this.tableData = res.data;
    });
  },
};
</script>
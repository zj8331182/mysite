<template>
  <div>
    <el-page-header content="添加员工" @back="back"> </el-page-header>
    <el-form ref="form" :model="form" label-width="100px" class="form">
      <el-form-item label="姓名">
        <el-input v-model="form.name" class="name"></el-input>
      </el-form-item>
      <el-form-item label="部门">
        <el-select v-model="form.department">
          <el-option
            v-for="department in departments"
            :key="department.value"
            :label="department.label"
            :value="department.value"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit" :loading="isLoading"
          >添加</el-button
        >
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  data() {
    return {
      departments: this.GLOBAL.allDepartments,
      form: {},
      isLoading: false,
    };
  },
  methods: {
    back() {
      this.$router.back();
    },
    submit() {
      this.isLoading = true;
      Axios.post(
        this.GLOBAL.baseUrl + "employee/",
        {
          name: this.form.name,
          department: this.form.department,
        },
        {
          header: {
            "X-CSRFToken": this.GLOBAL.getCookie("csrftoken"),
          },
        }
      )
        .then(() => {
          this.isLoading = false;
          this.$message({
            showClose: true,
            message: "操作成功",
            type: "success",
          });
        })
        .catch((err) => {
          this.isLoading = false;
          this.$message({
            showClose: true,
            message: err,
            type: "error",
          });
        });
    },
  },
};
</script>

<style>
.form {
  margin-top: 30px;
}
.name {
  width: 30%;
}
</style>
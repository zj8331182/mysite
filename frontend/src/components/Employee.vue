<template>
  <div v-loading="isLoading">
    <el-table :data="tableData" width="100%">
      <el-table-column label="名字">
        <template slot-scope="scope">
          <el-input
            v-if="scope.row.isEdit"
            auto-complete="true"
            class="name"
            v-model="editedEmployee.name"
            :placeholder="scope.row.name"
          ></el-input>
          <span v-else>{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="部门">
        <template slot-scope="scope">
          <el-select
            v-if="scope.row.isEdit"
            v-model="editedEmployee.department"
            :placeholder="getDepartmentName(scope.row.department)"
          >
            <el-option
              v-for="department in departments"
              :key="department.value"
              :label="department.label"
              :value="department.value"
            ></el-option>
          </el-select>
          <span v-else>{{ getDepartmentName(scope.row.department) }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-popconfirm
            v-if="scope.row.isEdit"
            title="确定要修改数据吗?"
            @confirm="handleClickUpdate(scope.row)"
          >
            <el-button slot="reference" type="success" size="mini"
              >确认</el-button
            >
          </el-popconfirm>
          <el-popconfirm
            v-else
            title="确定要删除该员工吗?"
            @confirm="handleClickDelete(scope.row)"
          >
            <el-button slot="reference" type="danger" size="mini"
              >移除</el-button
            >
          </el-popconfirm>
          <el-button
            v-if="scope.row.isEdit"
            type="danger"
            size="mini"
            @click="scope.row.isEdit = false"
            >取消</el-button
          >

          <el-button
            v-else
            type="primary"
            size="mini"
            @click="handleClickEdit(scope.row)"
            >修改</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" @click="handleClickAdd()" class="btnAdd"
      >添加</el-button
    >
  </div>
</template>
<style>
.btnAdd {
  margin-top: 20px;
}
.name {
  width: 150px;
}
</style>
<script>
import Axios from 'axios'
export default {
  data() {
    return {
      tableData: [],
      isLoading: true,
      departments: this.GLOBAL.allDepartments,
      editedEmployee: {},
      departmentsMap: new Map()
    }
  },
  methods: {
    handleClickDelete(row) {
      this.isLoading = true
      Axios.delete(this.GLOBAL.baseUrl + 'employee/' + row.id)
        .then(() => {
          this.showSuccess()
          this.fetchData()
        })
        .catch((err) => {
          this.showError(err)
        })
    },
    handleClickEdit(row) {
      row.isEdit = true
    },
    handleClickAdd() {
      this.$router.push('/employee/add')
    },
    handleClickUpdate(row) {
      Axios.put(this.GLOBAL.baseUrl + 'employee/' + row.id + '/', {
        name: this.editedEmployee.name,
        department: this.editedEmployee.department
      })
        .then(() => {
          this.showSuccess()
          row.isEdit = false
          row.name = this.editedEmployee.name
          row.department = this.editedEmployee.department
        })
        .catch((err) => {
          this.showError(err)
        })
    },
    fetchData() {
      Axios.get(this.GLOBAL.baseUrl + 'employee/')
        .then((res) => {
          this.isLoading = false
          var table = res.data
          table.forEach((item) => {
            item.isEdit = false
          })
          this.tableData = table
        })
        .catch((err) => {
          this.showError(err)
        })
    },
    showError(err) {
      this.isLoading = false
      this.$message({
        showClose: true,
        message: err,
        type: 'error'
      })
    },
    showSuccess() {
      this.$message({
        showClose: true,
        message: '操作成功',
        type: 'error'
      })
    },
    getDepartmentName(departmentCode) {
      return this.departmentsMap.get(departmentCode)
    }
  },
  mounted() {
    this.fetchData()
    this.departments.forEach((department) => {
      this.departmentsMap.set(department.value, department.label)
    })
  }
}
</script>

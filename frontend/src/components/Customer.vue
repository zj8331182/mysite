<template>
<div v-loading="isLoading">
    <el-table :data="tableData" width="100%">
        <el-table-column label="客户等级">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.level" :placeholder="scope.row.level" type="number"></el-input>
                <span v-else>{{ scope.row.level }}</span>
            </template>
        </el-table-column>
        <el-table-column label="客户名称">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.name" :placeholder="scope.row.name"></el-input>
                <span v-else>{{ scope.row.name }}</span>
            </template>
        </el-table-column>
        <el-table-column label="联系人">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.contract_people" :placeholder="scope.row.contract_people"></el-input>
                <span v-else>{{ scope.row.contract_people }}</span>
            </template>
        </el-table-column>
        <el-table-column label="联系方式">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.contract_tel" :placeholder="scope.row.contract_tel"></el-input>
                <span v-else>{{ scope.row.contract_tel }}</span>
            </template>
        </el-table-column>
        <el-table-column label="地址">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.address" :placeholder="scope.row.address"></el-input>
                <span v-else>{{ scope.row.address }}</span>
            </template>
        </el-table-column>
        <el-table-column label="支付方式">
            <template slot-scope="scope">
                <el-select v-if="scope.row.isEdit" v-model="editedCustomer.pay_way" :placeholder="getPayWayName(scope.row.pay_way)">
                    <el-option v-for="way in payWayMap.entries" :key="way.key" :label="way.value" :value="way.key"></el-option>
                </el-select>
                <span v-else>{{ getPayWayName(scope.row.pay_way) }}</span>
            </template>
        </el-table-column>
        <el-table-column label="优惠包">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.discount_package" :placeholder="scope.row.discount_package" type="number"></el-input>
                <span v-else>{{ scope.row.discount_package }}</span>
            </template>
        </el-table-column>
        <el-table-column label="负责人">
            <template slot-scope="scope">
                <el-select v-if="scope.row.isEdit" v-model="editedCustomer.res_person_name" :placeholder="scope.row.res_person_name" multiple filterable remote reserve-keyword :remote-method="requestEmployee" :loading="employeeLoading">
                    <el-option v-for="employee in employeeItems" :key="employee.id" :label="employee.name" :value="employee.id"></el-option>
                </el-select>
                <span v-else>{{ scope.row.res_person_name }}</span>
            </template>
        </el-table-column>
        <el-table-column label="最近联系">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.recent_contract_time" :placeholder="scope.row.recent_contract_time" type="date"></el-input>
                <span v-else>{{ scope.row.recent_contract_time }}</span>
            </template>
        </el-table-column>
        <el-table-column label="最近交易">
            <template slot-scope="scope">
                <span>{{ scope.row.recent_deal_time }}</span>
            </template>
        </el-table-column>
        <el-table-column label="备注">
            <template slot-scope="scope">
                <el-input v-if="scope.row.isEdit" auto-complete="true" class="name" v-model="editedCustomer.comment" :placeholder="scope.row.comment"></el-input>
                <span v-else>{{ scope.row.comment }}</span>
            </template>
        </el-table-column>
        <el-table-column label="操作">
            <template slot-scope="scope">
                <el-popconfirm v-if="scope.row.isEdit" title="确定要修改数据吗?" @confirm="handleClickUpdate(scope.row)">
                    <el-button slot="reference" type="success" size="mini">确认</el-button>
                </el-popconfirm>
                <el-popconfirm v-else title="确定要删除该员工吗?" @confirm="handleClickDelete(scope.row)">
                    <el-button slot="reference" type="danger" size="mini">移除</el-button>
                </el-popconfirm>
                <el-button v-if="scope.row.isEdit" type="danger" size="mini" @click="scope.row.isEdit = false">取消</el-button>

                <el-button v-else type="primary" size="mini" @click="handleClickEdit(scope.row)">修改</el-button>
            </template>
        </el-table-column>
    </el-table>
    <el-button type="primary" @click="handleClickAdd()" class="btnAdd">添加</el-button>
</div>
</template>

<style>
.btnAdd {
    margin-top: 20px;
}

.name {
    width: 100px;
}
</style>

<script>
import Axios from 'axios'
export default {
  data() {
    return {
      tableData: [],
      isLoading: true,
      editedCustomer: {},
      payWayMap: new Map(),
      employeeLoading: false,
      employeeItems: []
    }
  },
  methods: {
    handleClickDelete(row) {
      this.isLoading = true
      Axios.delete(this.GLOBAL.baseUrl + 'customer/' + row.id)
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
      this.$router.push('/customer/add')
    },
    handleClickUpdate(row) {
      Axios.put(this.GLOBAL.baseUrl + 'customer/' + row.id + '/', {
        name: this.editedCustomer.name,
        department: this.editedCustomer.department
      })
        .then(() => {
          this.showSuccess()
          row.isEdit = false
          row.name = this.editedCustomer.name
          row.department = this.editedCustomer.department
        })
        .catch((err) => {
          this.showError(err)
        })
    },
    fetchData() {
      Axios.get(this.GLOBAL.baseUrl + 'customer/')
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
    getPayWayName(payWap) {
      return this.payWayMap.get(payWap)
    },
    requestEmployee(query) {
      Axios.get(this.GLOBAL.baseUrl + 'employee/')
        .then((res) => {
          this.employeeLoading = false
          var table = res.data
          this.employeeItems = table.filter(item => {
            return item.name.toLowerCase().indexOf(query.toLowerCase()) > -1
          }).map(i => {
            return {
              'id': i.id,
              'name': i.name
            }
          })
        })
        .catch((err) => {
          this.showError(err)
        })
    }
  },
  mounted() {
    this.fetchData()
    this.payWayMap.set(0, '现金')
    this.payWayMap.set(1, '微信')
    this.payWayMap.set(2, '支付宝')
    this.payWayMap.set(3, '转账')
  }
}
</script>

<template>
  <el-container style="border: 1px solid #eee; height: 100%">
    <el-header>
      <span>XXX灯箱后台管理系统</span>
    </el-header>
    <el-container>
      <el-aside width="20%" style="border: 1px solid #eee">
        <el-menu :default-active="$router.path" router>
          <el-menu-item index="/employee"> 员工管理 </el-menu-item>
          <el-menu-item index="/customer" route="customer">
            客户管理
          </el-menu-item>
          <el-menu-item index="/order" route="order"> 订单管理 </el-menu-item>
        </el-menu>
      </el-aside>

      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>
<style>
.el-menu-item {
  text-align: center;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
html,
body,
#app {
  height: 100%;
}
</style>

<script>
export default {};
</script>

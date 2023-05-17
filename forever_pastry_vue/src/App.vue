<template>
 <div id="wrapper">
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>ForEver_Pastry</strong></router-link>

      <!--let us making the hamburgers -->
      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click= "showMobileMenu = !showMobileMenu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
<!--when showMobile is "is-active" and cliked on burger the div will appear-->
    <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
      <div class="navbar-end">
        <router-link to="/pastrys" class="navbar-item">Pastrys</router-link>
        <router-link to="/bakerys" class="navbar-item">Bakerys</router-link>

        <!--buttons for login and shopping cart -->
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/log-in" class="button is-light">Log-in</router-link>
            <router-link to="/cart" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>

      </div>
    </div>
  </nav>

  <section class="section">
    <!--router-view : The <router-view> component is responsible for rendering the appropriate component based on the current route.-->
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2023</p>
  </footer>

 </div>
</template>

<!--set-up the mobile-screen-->
<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma'
</style>

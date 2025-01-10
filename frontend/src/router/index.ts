import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw, RouteLocationNormalized, NavigationGuardNext } from 'vue-router'
import { useUserStore } from '@/stores/user.ts'
import axios from 'axios'

const checkAuth = (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) => {
  const useStore = useUserStore()
  if (!useStore.userToken) {
    next({ name: "Auth" })
  } else {
    if (to.path != '/auth') {
      next()
    } else {
      next({ path: to.path })
    }
  }
}

const checkTeacher = async (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: NavigationGuardNext
) => {
  const useStore = useUserStore()
  try {
    const json = {
      token: useStore.userToken
    }
    const { data } = await axios.post("/users/isTeacher", json);
    if (data === "True") {
      next()
    } else {
      next({ name: "home" })
    }
  } catch (err) {
    console.log(err);
  }
}

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomePage.vue'),
    beforeEnter: checkAuth
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/AuthPage.vue')
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: () => import('../views/TasksPage.vue'),
    beforeEnter: checkAuth
  },
  {
    path: '/tests',
    name: 'Tests',
    component: () => import('../views/TestsPage.vue'),
    beforeEnter: checkAuth
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: () => import('../views/TeacherPanel.vue'),
    beforeEnter: checkTeacher
  },
  {
    path: '/test/:id',
    name: 'Test',
    component: () => import('../views/TestPage.vue'),
    beforeEnter: checkAuth
  },
  {
    path: '/statistics/test/:id',
    name: 'Statistics For Test',
    component: () => import('../views/TestStatisticsPage.vue'),
    beforeEnter: checkTeacher
  },
  {
    path: '/statistics/user/:id',
    name: 'Statistics For User',
    component: () => import('../views/UserStatisticsPage.vue'),
    beforeEnter: checkTeacher
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
})

export default router

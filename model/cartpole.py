import numpy as np
import matplotlib.pyplot as plt

class CartPole:
    def __init__(self, dt, y, y_dot, th, th_dot, M, m, l, g) -> None:
        self.dt = dt
        self.y = y
        self.y_dot = y_dot 
        self.th = th
        self.th_dot = th_dot
        self.M = M
        self.m = m
        self.l = l
        self.g = g

    def forward(self, u):
        self.y      += self.y_dot*self.dt
        self.th     += self.th_dot*self.dt
        self.y_dot  += ((u + self.m*np.sin(self.th)*(self.l*self.th_dot**2 + self.g*np.cos(self.th)))/(self.M+self.m*np.sin(self.th)**2))*self.dt
        self.th_dot += ((-u*np.cos(self.th) - self.m*self.l*self.th**2*np.cos(self.th)*np.sin(self.th) - (self.M + self.m)*self.g*np.sin(self.th))/(self.l*(self.M + self.m*np.sin(self.th)**2)))*self.dt

    def get_state(self):
        x = np.array([self.y, self.th, self.y_dot, self.th_dot])

        return x

if __name__ == "__main__":
    sim_time = 10
    dt = 1e-3
    max_step = int(sim_time / dt)
    state_traj = np.zeros((max_step, 4))
    cartpole = CartPole(dt=dt,
                        y = 0,
                        y_dot = 0, 
                        th = 3,
                        th_dot = 0,
                        M = 2,
                        m = 0.2,
                        l = 0.5,
                        g = 9.8)
    for i in range(max_step):
        cartpole.forward(u=0)
        state_traj[i,:] = cartpole.get_state()

    fig = plt.figure()
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    y_fig = fig.add_subplot(2, 2, 1)
    th_fig = fig.add_subplot(2, 2, 2)
    y_dot_fig = fig.add_subplot(2, 2, 3)
    th_dot_fig = fig.add_subplot(2, 2, 4)
    y_fig.set_title(r"y")
    y_fig.plot(state_traj[:,0])
    th_fig.set_title(r"\theta")
    th_fig.plot(state_traj[:,1])
    y_dot_fig.set_title(r"y_dot")
    y_dot_fig.plot(state_traj[:,2])
    th_dot_fig.set_title(r"\theta_dot")
    th_dot_fig.plot(state_traj[:,3])
    
    plt.legend()
    plt.show()
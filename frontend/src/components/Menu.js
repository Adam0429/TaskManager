import React, { Component } from 'react';
import { Menu, Switch } from 'antd';
import * as icon from '@ant-design/icons';

const { SubMenu } = Menu;

export default class tasktable extends Component {
    state = {
      theme: 'light',
      current: '1',
    };
  
    changeTheme = value => {
      this.setState({
        theme: value ? 'light' : 'dark',
      });
    };
  
    handleClick = e => {
      console.log('click ', e);
      this.setState({
        current: e.key,
      });
    };
  
    render() {
      return (
        
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']} defaultOpenKeys={['sub1']}>
          <SubMenu key="sub1" icon={<icon.CodeOutlined />} title="任务">
            <Menu.Item key="1">普通任务</Menu.Item>
            <Menu.Item key="2">定时任务</Menu.Item>
          </SubMenu>
          <Menu.Item key="3" icon={<icon.DesktopOutlined />}>
            监控
          </Menu.Item>
          <Menu.Item key="4" icon={<icon.SettingOutlined />}>
            设置
          </Menu.Item>
          <Menu.Item key="5" icon={<icon.ToolOutlined />}>
            工具
          </Menu.Item>
          <Menu.Item key="6" icon={<icon.CopyOutlined />}>
            日志
          </Menu.Item>
      </Menu>
      );
    }
  }
  

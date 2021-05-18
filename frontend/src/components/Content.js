import React, { Component } from 'react';
import { Layout } from 'antd';
import PubSub from 'pubsub-js' 
import NormalTaskPage from '../NormalTask/page'
import LoopTaskPage from '../LoopTask/page'

const { Header, Content, Footer, Sider } = Layout;

export default class content extends Component {
    constructor(props) {
        super(props);
        this.state = {
            menu:1
        };

        PubSub.subscribe('menu', (msg, data) => {
            console.log( msg, data );
            this.setState({
                menu: data,
            });
        });
    }
      
    render() {
        let {menu} = this.state
        if(menu==1){
            var page = <NormalTaskPage/>
        }
        else if(menu==2){
            var page = <LoopTaskPage/>
        }
        return (
            <Content>
                {page}
            </Content>

        );
      }
    }
    
  
import React from 'react';

import AppBar from 'material-ui/AppBar';
import Drawer from 'material-ui/Drawer';
import Menu from 'material-ui/Menu';
import MenuItem from 'material-ui/MenuItem';
import IconButton from 'material-ui/IconButton';
import {Card, CardMedia, CardTitle} from 'material-ui/Card';
import Divider from 'material-ui/Divider';

import Assistant from 'material-ui/svg-icons/image/assistant';
import NavigationOpen from 'material-ui/svg-icons/navigation/menu';
import HelpOutline from 'material-ui/svg-icons/action/help-outline';

class UniNavigationBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {open: false};

        this.updateDimensions = this.updateDimensions.bind(this);

        this.handleToggle = () => this.setState({open: !this.state.open});
        this.handleClose = () => this.setState({open: false});
    }

    componentDidMount(){
        this.updateDimensions();
        window.addEventListener("resize", this.updateDimensions);
    }

    updateDimensions() {
        this.setState({
            height: window.innerHeight,
            footerHeight: document.getElementById('leftNavFooter').clientHeight
        });
    }

    render() {
        return (
            <div>
                <AppBar
                    title="UniStack"
                    iconElementLeft={
                        <IconButton
                            onTouchTap={this.handleToggle.bind(this)}
                        >
                            <NavigationOpen />
                        </IconButton>
                    }
                />

                <Drawer
                    docked={false}
                    open={this.state.open}
                    onRequestChange={(open) => this.setState({open})}
                >
                    <div
                        style={{
                            overflowY: 'auto',
                            overflowX: 'hidden',
                            height: (this.state.height - this.state.footerHeight) + 'px'}}
                    >
                        <Card >
                            <CardMedia
                                overlay={
                                    <div>
                                        <CardTitle
                                            title="UniStack"
                                            subtitle="Slogan"
                                            titleColor="#FFFFFF"
                                            subtitleColor="#FFFFFF"/>
                                    </div>
                                }
                            >
                                <img src="/static/images/left_nav_wallpaper.jpg" />
                            </CardMedia>
                        </Card>
                        <Menu>
                            <MenuItem primaryText="item 1" leftIcon={<Assistant />} />
                            <MenuItem primaryText="item 2" />
                            <MenuItem primaryText="item 3" />
                        </Menu>
                    </div>
                    <div id="leftNavFooter" style={{position: 'absolute', bottom: 0, width: '100%', overflow: 'hidden'}}>
                        <Divider />
                        <Menu>
                            <MenuItem primaryText="item bottom" />
                            <MenuItem primaryText="Help & About" leftIcon={<HelpOutline />} />
                        </Menu>
                    </div>

                </Drawer>
            </div>
        );
    }
}

export default UniNavigationBar;

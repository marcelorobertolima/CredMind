import CodeDialog from "@/app/components/shared/CodeDialog";
import React from "react";
const FullScreenCode = () => {
  return (
    <>
      <CodeDialog>
        {`
"use client";
import {
  Button,
  Dialog,
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  List,
  ListItemText,
  Divider,
} from '@mui/material';
import Slide from '@mui/material/Slide';
import { IconX } from '@tabler/icons-react';

const Transition = React.forwardRef(function Transition(props, ref)
{
  return <Slide direction="up" ref={ref} {...props} />;
});
const FullscreenDialog = () => {
const [open, setOpen] = React.useState(false);

const handleClickOpen = () => {
    setOpen(true);
};

const handleClose = () => {
    setOpen(false);
};


return (
    <>
      <Button variant="contained" color="error" fullWidth onClick={handleClickOpen}>
        Open Fullscreen Dialog
      </Button>
      <Dialog fullScreen open={open} onClose={handleClose} TransitionComponent={Transition}>
        <AppBar sx={{ position: 'relative' }}>
          <Toolbar>
            <IconButton edge="start" color="inherit" onClick={handleClose} aria-label="close">
              <IconX width={24} height={24} />
            </IconButton>
          <Typography
            variant="h6"
            component="div"
            sx={{
              ml: 2,
              flex: 1
            }}>
              Sound
            </Typography>
            <Button autoFocus color="inherit" onClick={handleClose}>
              Save
            </Button>
          </Toolbar>
        </AppBar>
        <List>
          <ListItemButton>
            <ListItemText primary="Phone ringtone" secondary="Titania" />
         </ListItemButton>
        <Divider />
        <ListItemButton>
          <ListItemText primary="Default notification ringtone" secondary="Tethys" />
        </ListItemButton>
        </List>
      </Dialog>
    </>
);`}
      </CodeDialog>
    </>
  );
};

export default FullScreenCode;
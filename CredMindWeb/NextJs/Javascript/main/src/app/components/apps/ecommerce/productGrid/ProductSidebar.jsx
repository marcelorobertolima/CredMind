"use client"
import React from 'react';
import Drawer from '@mui/material/Drawer';
import useMediaQuery from '@mui/material/useMediaQuery';
import ProductFilter from './ProductFilter';

const drawerWidth = 250;


const ProductSidebar = ({ isMobileSidebarOpen, onSidebarClose }) => {
  const lgUp = useMediaQuery((theme) => theme.breakpoints.up('lg'));

  return (
    <Drawer
      open={isMobileSidebarOpen}
      onClose={onSidebarClose}
      variant={lgUp ? 'permanent' : 'temporary'}
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        zIndex: lgUp ? 0 : 1,
        [`& .MuiDrawer-paper`]: { position: 'relative' },
      }}
    >
      {/* ------------------------------------------- */}
      {/* Filter Sidebar */}
      {/* ------------------------------------------- */}
      <ProductFilter />
    </Drawer>
  );
};


export default ProductSidebar;

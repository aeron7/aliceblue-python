from ctypes import Structure
import ctypes, struct
from struct import pack_into


# class for reading bytes
class CliMarketdataRes(Structure):
    _pack_ = 1
    _fields_ = [
        ('mode', ctypes.c_int8),
        ('exchange_code', ctypes.c_uint8),
        ('instrument_token', ctypes.c_uint32),
        ('last_traded_price', ctypes.c_uint32),
        ('last_traded_time', ctypes.c_uint32),
        ('last_traded_quantity', ctypes.c_uint32),
        ('trade_volume', ctypes.c_uint32),
        ('best_bid_price', ctypes.c_uint32),
        ('best_bid_quantity', ctypes.c_uint32),
        ('best_ask_price', ctypes.c_uint32),
        ('best_ask_quantity', ctypes.c_uint32),
        ('total_buy_quantity', ctypes.c_uint64),
        ('total_sell_quantity', ctypes.c_uint64),
        ('average_trade_price', ctypes.c_uint32),
        ('exchange_timestamp', ctypes.c_uint32),
        ('open_price', ctypes.c_uint32),
        ('high_price', ctypes.c_uint32),
        ('low_price', ctypes.c_uint32),
        ('close_price', ctypes.c_uint32),
        ('yearly_high_price', ctypes.c_uint32),
        ('yearly_low_price', ctypes.c_uint32),
    ]
    size = 86

    def get_CliMarketdataRes_Instruct(self, packet_buffer):
        self.mode = struct.unpack('>b', packet_buffer[0:1])[0]
        self.exchange_code = struct.unpack('>b', packet_buffer[1:2])[0]
        self.instrument_token = struct.unpack('>I', packet_buffer[2:6])[0]
        self.last_traded_price = struct.unpack('>I', packet_buffer[6:10])[0]
        self.last_traded_time = struct.unpack('>I', packet_buffer[10:14])[0]
        self.last_traded_quantity = struct.unpack('>I', packet_buffer[14:18])[0]
        self.trade_volume = struct.unpack('>I', packet_buffer[18:22])[0]
        self.best_bid_price = struct.unpack('>I', packet_buffer[22:26])[0]
        self.best_bid_quantity = struct.unpack('>I', packet_buffer[26:30])[0]
        self.best_ask_price = struct.unpack('>I', packet_buffer[30:34])[0]
        self.best_ask_quantity = struct.unpack('>I', packet_buffer[34:38])[0]
        self.total_buy_quantity = struct.unpack('>Q', packet_buffer[38:46])[0]
        self.total_sell_quantity = struct.unpack('>Q', packet_buffer[46:54])[0]
        self.average_trade_price = struct.unpack('>I', packet_buffer[54:58])[0]
        self.exchange_timestamp = struct.unpack('>I', packet_buffer[58:62])[0]
        self.open_price = struct.unpack('>I', packet_buffer[62:66])[0]
        self.high_price = struct.unpack('>I', packet_buffer[66:70])[0]
        self.low_price = struct.unpack('>I', packet_buffer[70:74])[0]
        self.close_price = struct.unpack('>I', packet_buffer[74:78])[0]
        self.yearly_high_price = struct.unpack('>I', packet_buffer[78:82])[0]
        self.yearly_low_price = struct.unpack('>I', packet_buffer[82:86])[0]
